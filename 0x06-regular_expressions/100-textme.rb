#!/usr/bin/env ruby

message = ARGV[0]
sender = message.match(/\[from:(.*?)\]/)
recever = message.match(/\[to:(.*?)\]/)
flags = message.match(/\[flags:(.*?)\]/)
puts "#{sender[1]},#{recever[1]},#{flags[1]}"
