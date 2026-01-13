import mongoose from 'mongoose';

async function conectaNaDataBase() {

    await mongoose.connect(process.env.DB_CONECTION_STRING);
    
    return mongoose.connection;
}

export default conectaNaDataBase;