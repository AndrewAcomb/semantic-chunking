
require 'glim_ai'
require 'json'

#  first command line argument is the output directory
if ARGV.length < 1
    puts "Usage: ruby make_chunks.rb <output_dir>"
    exit
end

@output_dir = ARGV[0]
Dir.mkdir(@output_dir) unless File.exist?(@output_dir)

@glim = GlimContext.new

def generate_chunks(input_path)
    puts ("Processing all files in #{input_path}...")

    file_data = {}
    Dir.glob(input_path) do |file|
        item = {}
        puts ("Processing #{file}...")
        input = File.read(file)
        item[:input] = input
        request = @glim.request_from_template('chunker1', input:)
        future = request.send_and_return_future
        item[:future] = future
        file_data[file] = item
        break if file_data.length >= 12
    end

    file_data.each do |file, item|
        puts ("Waiting for results for #{file}...")
        future = item[:future]
        response = future.await_response
        completion = response.completion
        json = JSON.parse(completion)
        json = {file: file, original: item[:input], chunks: json}
        json_text = JSON.pretty_generate(json)
        output_path = File.join(@output_dir, File.basename(file, File.extname(file))+".json")
        puts ("Writing #{output_path}...")
        File.write(output_path, json_text)
        puts "Cost so far: $ #{'%5.2f' % @glim.cost}"
    end


end

generate_chunks("raw_text/*.txt")

# puts chunks.join("\n\n")