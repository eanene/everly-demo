require 'sinatra'

set :bind, '0.0.0.0'

get '/app-1' do
  'This is the Rails Microservice, the everwell experience!'
end
