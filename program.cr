# Odd-Even Pascal's Triangle

print "Enter number of rows to print: "
rows = gets.to_s.to_i
puts

first_row = [1]
last_row = [1, 1]

j = 1
while j < rows
  print " "
  j += 1
end

first_row.each do |i|
  print "▲"
end

puts

j = 1
while j < rows - 1
  print " "
  j += 1
end

last_row.each do |i|
  print "▲ "
end

next_row = last_row.clone

index = 0
iteration = 2

while iteration < rows
  puts ""
  
  next_row = Array.new(last_row.size + 1, 0)
  
  last_row.unshift(0)
  shifted_row = last_row.clone
  last_row.shift
  last_row.push(0)
  
  while index < next_row.size
    next_row[index] = last_row[index] + shifted_row[index]
    index += 1
  end
  
  index = 0
  
  j = 1
  while j < (rows - iteration)
    print " "
    j += 1
  end
  
  next_row.each do |i|
    if i.even?
      print "  "
    else
      print "▲ "
    end
  end
  
  iteration += 1
  last_row = next_row.clone
end