# frozen_string_literal: true

source 'https://rubygems.org'

gem 'dotenv'
gem 'rake', '~> 13.0'
gem 'minitest', '~> 5.0'
gem 'anthropic'
gem 'ruby-openai'
gem 'json-schema'

gem 'tiktoken_ruby'

gem 'nokogiri'

if File.exist?('../glim')
    puts "using local glim_ai gem"
    gem 'glim_ai', path: '../glim'
else
    puts "using remote glim_ai gem from rubygems"
    gem 'glim_ai', '0.3.0'
end

# gem "tiktoken_ruby", "~> 0.0.5"

