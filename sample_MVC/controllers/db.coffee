mongoClient = require('mongodb').MongoClient

module.exports = {
  save: (req,res)->
    mongoClient.connect("mongodb://localhost:27017/testDB", (e,db)->
      if e
        return
      db.collection("details", (e,coll)->
        coll.insert(req.body)
        console.log "Entry inserted "
        res.redirect('/new-entry')
      )
    )

  getFromDB: (callback)->
    mongoClient.connect("mongodb://localhost:27017/testDB", (e,db)=>
      if e
        return
      db.collection("details", (e,coll)=>
        coll.find().toArray( (e,items)=>
          return callback(items)
        )
      )
    )

  list : (callback)->
    @getFromDB (items)->
      return callback(items)

}