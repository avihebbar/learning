db = require './db'
async = require 'async'

module.exports = {
  new : (req, res)->
    res.render 'data/new',

  save : (req,res)->
    console.log req.body
    db.save(req,res)

  list :(req,res)->
    db.list( (list)->
      console.log list
      res.render 'data/list',
        entries:list
    )
}
