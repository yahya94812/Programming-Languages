// ==========================================
// CONNECTION OPERATIONS
// ==========================================

// Connect to a MongoDB instance running locally
mongosh

// Connect to a specific MongoDB instance with authentication
mongosh "mongodb://username:password@hostname:port/database"

// Connect to a MongoDB Atlas cluster
mongosh "mongodb+srv://username:password@cluster0.example.mongodb.net/database"

// Switch to a database (creates it if it doesn't exist)
use myDatabase

// Display current database
db

// Show all databases
show dbs

// Show all collections in current database
show collections

// ==========================================
// CREATE OPERATIONS
// ==========================================

// Create a new collection (implicitly)
db.newCollection.insertOne({ name: "First Document" })

// Create a new collection (explicitly)
db.createCollection("customers")

// Insert a single document
db.customers.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  address: {
    street: "123 Main St",
    city: "New York",
    state: "NY",
    zip: "10001"
  },
  tags: ["premium", "loyal"],
  created: new Date()
})

// Insert multiple documents
db.customers.insertMany([
  {
    name: "Jane Smith",
    email: "jane@example.com",
    age: 25,
    address: {
      street: "456 Oak Ave",
      city: "Chicago",
      state: "IL",
      zip: "60007"
    },
    tags: ["new"],
    created: new Date()
  },
  {
    name: "Bob Johnson",
    email: "bob@example.com",
    age: 42,
    address: {
      street: "789 Pine Rd",
      city: "Seattle",
      state: "WA",
      zip: "98101"
    },
    tags: ["premium"],
    created: new Date()
  }
])

// ==========================================
// READ OPERATIONS
// ==========================================

// Find all documents in a collection
db.customers.find()

// Find all documents with pretty formatting
db.customers.find().pretty()

// Find the first document
db.customers.findOne()

// Find documents with specific criteria
db.customers.find({ age: 30 })

// Find with multiple criteria (AND)
db.customers.find({ age: 30, name: "John Doe" })

// Find with OR condition
db.customers.find({
  $or: [
    { age: 30 },
    { name: "Jane Smith" }
  ]
})

// Find with comparison operators
db.customers.find({ age: { $gt: 30 } })  // greater than
db.customers.find({ age: { $gte: 30 } }) // greater than or equal
db.customers.find({ age: { $lt: 30 } })  // less than
db.customers.find({ age: { $lte: 30 } }) // less than or equal
db.customers.find({ age: { $ne: 30 } })  // not equal

// Find with in operator
db.customers.find({ age: { $in: [25, 30, 35] } })

// Find documents with specific fields (projection)
db.customers.find({}, { name: 1, email: 1 }) // Include only name and email
db.customers.find({}, { address: 0 }) // Exclude address

// Find documents with query on nested fields
db.customers.find({ "address.city": "New York" })

// Find documents with array queries
db.customers.find({ tags: "premium" })          // Contains "premium"
db.customers.find({ tags: { $all: ["premium", "loyal"] } }) // Contains all
db.customers.find({ tags: { $size: 2 } })       // Array size is 2

// Count documents
db.customers.countDocuments()
db.customers.countDocuments({ age: { $gt: 30 } })

// Limit results
db.customers.find().limit(2)

// Skip results (pagination)
db.customers.find().skip(1).limit(2)

// Sort results
db.customers.find().sort({ age: 1 })  // Ascending
db.customers.find().sort({ age: -1 }) // Descending
db.customers.find().sort({ name: 1, age: -1 }) // Sort by multiple fields

// ==========================================
// UPDATE OPERATIONS
// ==========================================

// Update a single document (replace entire document except _id)
db.customers.replaceOne(
  { name: "John Doe" },
  {
    name: "John Doe",
    email: "john.new@example.com",
    age: 31,
    address: {
      street: "456 New St",
      city: "Los Angeles",
      state: "CA",
      zip: "90001"
    },
    tags: ["premium", "loyal", "updated"],
    updated: new Date()
  }
)

// Update specific fields in a single document
db.customers.updateOne(
  { name: "Jane Smith" },
  {
    $set: {
      age: 26,
      "address.city": "San Francisco",
      updated: new Date()
    }
  }
)

// Update specific fields in multiple documents
db.customers.updateMany(
  { tags: "premium" },
  {
    $set: {
      status: "VIP",
      updated: new Date()
    }
  }
)

// Increment numeric fields
db.customers.updateOne(
  { name: "Bob Johnson" },
  {
    $inc: { age: 1 },
    $set: { updated: new Date() }
  }
)

// Add elements to arrays
db.customers.updateOne(
  { name: "Bob Johnson" },
  {
    $push: { tags: "referral" }
  }
)

// Add multiple elements to arrays
db.customers.updateOne(
  { name: "John Doe" },
  {
    $push: { 
      tags: { 
        $each: ["sale", "discount"] 
      } 
    }
  }
)

// Remove elements from arrays
db.customers.updateOne(
  { name: "John Doe" },
  {
    $pull: { tags: "sale" }
  }
)

// Upsert (update if exists, insert if doesn't)
db.customers.updateOne(
  { email: "sarah@example.com" },
  {
    $set: {
      name: "Sarah Williams",
      age: 35,
      created: new Date()
    }
  },
  { upsert: true }
)

// ==========================================
// DELETE OPERATIONS
// ==========================================

// Delete a single document
db.customers.deleteOne({ name: "Jane Smith" })

// Delete multiple documents
db.customers.deleteMany({ age: { $lt: 30 } })

// Delete all documents in a collection
db.customers.deleteMany({})

// Delete a collection
db.customers.drop()

// Delete the current database
db.dropDatabase()

// ==========================================
// AGGREGATION OPERATIONS
// ==========================================

// Simple aggregation (similar to find)
db.customers.aggregate([
  { $match: { age: { $gt: 30 } } }
])

// Group by and count
db.customers.aggregate([
  {
    $group: {
      _id: "$address.state",
      count: { $sum: 1 }
    }
  }
])

// Group by and calculate statistics
db.customers.aggregate([
  {
    $group: {
      _id: "$address.state",
      averageAge: { $avg: "$age" },
      minAge: { $min: "$age" },
      maxAge: { $max: "$age" },
      count: { $sum: 1 }
    }
  }
])

// Multi-stage aggregation pipeline
db.customers.aggregate([
  { $match: { tags: "premium" } },
  { $project: { 
      _id: 0,
      name: 1, 
      email: 1, 
      state: "$address.state" 
    } 
  },
  { $sort: { name: 1 } }
])

// Lookup (join) aggregation
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "customer_info"
    }
  }
])

// ==========================================
// INDEX OPERATIONS
// ==========================================

// Create a single field index
db.customers.createIndex({ email: 1 }) // 1 for ascending, -1 for descending

// Create a unique index
db.customers.createIndex({ email: 1 }, { unique: true })

// Create a compound index
db.customers.createIndex({ age: 1, name: 1 })

// Create a text index for text search
db.products.createIndex({ description: "text" })

// Create a geospatial index
db.locations.createIndex({ coordinates: "2dsphere" })

// List all indexes on a collection
db.customers.getIndexes()

// Remove an index
db.customers.dropIndex("email_1")

// ==========================================
// ADMINISTRATION OPERATIONS
// ==========================================

// Get server status
db.serverStatus()

// Get collection statistics
db.customers.stats()

// Get database statistics
db.stats()

// Run a command
db.runCommand({ serverStatus: 1 })

// Get current operations
db.currentOp()

// Kill a specific operation
db.killOp(opId)

// ==========================================
// USER ADMINISTRATION
// ==========================================

// Create a user for a specific database
db.createUser({
  user: "appAdmin",
  pwd: "password123",
  roles: [
    { role: "readWrite", db: "myDatabase" },
    { role: "read", db: "analytics" }
  ]
})

// Show all users for current database
db.getUsers()

// Update a user's roles
db.updateUser("appAdmin",
  {
    roles: [
      { role: "readWrite", db: "myDatabase" },
      { role: "readWrite", db: "analytics" },
      { role: "read", db: "reporting" }
    ]
  }
)

// Change a user's password
db.changeUserPassword("appAdmin", "newPassword456")

// Remove a user
db.dropUser("appAdmin")
