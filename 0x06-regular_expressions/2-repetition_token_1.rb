#!/usr/bin/env ruby

#Find the regular expression that will match the above cases
# htn, hbtn

puts ARGV[0].scan(/hb{0,1}tn/).join
