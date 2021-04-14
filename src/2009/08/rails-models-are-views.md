---
title: 'rails models are views?'
date: '2009-08-31T19:07:10-07:00'
status: publish
exported_permalink: /2009/08/rails-models-are-views
author: sarah
excerpt: ''
type: post
id: 2032
category:
    - code
tag: []
post_format: []
---
Rails appears pretty strict about separation of the abstraction layers that make up its notion of a web application: models, view and controllers. If you were to suggest calling a presentation method, such as url\_for, in your model, the stoic Rails advocate will have an allergic reaction. However, Rails thinks nothing of rendering a model directly as a view, such as:

```

format.json { render :json => @products }
```

Now, one might argue that this is controller code and the controller is allowed to interpret the model as a view. The controller’s job is to mediate this interaction. However, I feel that it is a dangerous shortcut, made even more so by how hard to seems to be to override. Perhaps the json implementation is simply incomplete.

In xml, this strange controller pattern is easily corrected by [providing an xml view](http://danengle.us/2009/05/generating-custom-xml-for-your-rails-app/). The xml builder syntax is particularly readable, and it is easy to design your XML API effectively.

I haven’t found an equivalent for json. I tried to use a JSON API today to no avail. My model included image data which breaks when auto-rendered in JSON. What I really wanted was to include a URL instead of the image data, which I implement neatly in my xml.builder view:

```

xml.instruct!
xml.products("type"=>"array") do
  @products.each do |product|
    xml.product do
      xml.sku product.sku
      xml.name product.name
      xml.brand product.brand
      xml.img_url url_for(:controller => :products, :action => :show, :format=>:png, :id => product.id, :only_path => false)
    end
  end
end
```

The problem is that I want a similar view in JSON. The to\_json API leads me to put this logic in my model (gasp!). In fact, the ActiveRecord::Serialization docs give an example of providing a method to generate JSON instead of a literal attribute. The example is of a “permalink” which seem suspiciously like something that belongs is the view layer.

```

  konata.to_json(:methods => :permalink)
  # => {"id": 1, "name": "Konata Izumi", "age": 16,
        "created_at": "2006/08/01", "awesome": true,
        "permalink": "1-konata-izumi"}
```

Today’s solution was to go back to using my comfortable old XML API, but I would prefer to consume JSON from the other side. I wonder if anyone is working on a JSON builder or if there is some clear solution that I haven’t yet stumbled upon.