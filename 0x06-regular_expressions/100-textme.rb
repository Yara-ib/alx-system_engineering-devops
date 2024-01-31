#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([+A-Za-z0-9]+)\]\s\[to:([+A-Za-z0-9]+)\]\s\[flags:(.*?)\]/).join(',')
