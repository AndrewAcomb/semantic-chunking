
require 'glim_ai'



def generate_chunks(input)
    glim = GlimContext.new
    request = glim.request_from_template('chunker1.erb', input)
    future = request.send_and_return_future
    result = future.await_response
    puts result.completion

end

input = File.read('input.txt')

chunks = generate_chunks(input)

# puts chunks.join("\n\n")