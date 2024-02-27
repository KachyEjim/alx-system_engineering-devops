#!/usr/bin/env ruby

# Find the regular expression that will match the above cases
# hbttn, hbtttn, hbttttn, hbtttttn.

puts ARGV[0].scan(/hbt{2,5}n/).join
