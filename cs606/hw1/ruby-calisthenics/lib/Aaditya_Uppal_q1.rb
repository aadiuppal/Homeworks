module FunWithStrings
  def palindrome?
    s=self.downcase.scan(/\w/)#convert to lower case and use regex to look for non special characters
    return s==s.reverse#compare if  reverse string equals original string
    # your code here
  end
  def count_words
    self.downcase!
    s=self.split(' ').join(' ')
    list=s.split(/\W+/)
    h=Hash.new
    list.each do |i|
      if h.has_key?(i)
        h[i]+=1
      else
        h[i]=1
      end
    end
    return h
    # your code here
  end
  def anagram_groups
    list=self.split(/\W+/)
    h=Hash.new
    for i in list
      if h.has_key?(i.chars.sort.join)
        h[i.downcase.split('').sort.join].push(i)
      else
        h[i.downcase.split('').sort.join]=Array.[](i)
      end
    end
    ans=Array.[]()
    for k in h.keys
      ans.push(h[k])
    end
    return ans
    # your code here
  end
end

# make all the above functions available as instance methods on Strings:

class String
  include FunWithStrings
end
