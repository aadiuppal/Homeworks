class Class
  attr_reader:history
  def attr_accessor_with_history(attr_name)
    attr_name = attr_name.to_s # make sure it's a string
    attr_reader attr_name # create the attribute's getter
    attr_reader attr_name+"_history" # create bar_history getter
    class_eval %Q{
      # YOUR CODE HERE
      def #{attr_name}=(val)#setter for attr and attr_history
        if @#{attr_name}_history==nil
          @#{attr_name}_history=[]#if no history init history as blank array
        end
        @#{attr_name}_history.push(@#{attr_name})#if add prev attr to history
        @#{attr_name}=val#set current value to attr
      end
    }
  end
end
