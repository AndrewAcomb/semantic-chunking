
require 'glim_ai'



def generate_chunks(input)
    glim = GlimContext.new
    r = glim.request(model_id: chunking_model).await_response


end


input = File.read('input.txt')

chunks = generate_chunks(input)

puts chunks.join("\n\n")