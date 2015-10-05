class Dessert
  attr_accessor:name
  attr_accessor:calories
  def initialize(name, calories)
    @name=name
    @calories=calories
    # your code here
  end
  def healthy?
    if (@calories<200)
      return TRUE
    else
      return FALSE
    end
    # your code here
  end
  def delicious?
    return TRUE
    # your code here
  end
end

class JellyBean < Dessert
  attr_accessor:flavor
  def initialize(flavor)
    @flavor=flavor
    super(@flavor+" jelly bean", 5)
    # your code here
  end
  def delicious?
    if (@flavor=="licorice")
      return FALSE
    else
      return TRUE
    end
  end
end
