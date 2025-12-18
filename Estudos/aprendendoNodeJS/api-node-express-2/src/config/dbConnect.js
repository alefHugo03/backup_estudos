import mongoose from "mongoose"

mongoose.connect(process.env.DB_CONECT_MONGO);

let db = mongoose.connection;

export default db;