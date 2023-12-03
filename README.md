# semantic-chunking
Project for the Tools For Thought Hackathon at AGI House



# Tools

## Glim
If you're coding in Ruby and want to use the glim library:
https://github.com/uhgall/glim/
Clone this into a directory called "glim" at the same level as semantic-chunking.
Then:
cp .env.sample .env 
Edit file to put in your API_KEYS
bundle
Optionally, test if it's working: (Cost: $0.05 or so)
bundle exec glim_list_models 

# Modules

## semchunk
Code for using the semantic chunking technique.
Text file in, text file out.

bundle exec ruby semchunk/make_chunks.rb output/semchunk1
This reads the first 10 files from raw/ and puts the results in output/semchunk1.

Edit the prompt in chunker1.erb