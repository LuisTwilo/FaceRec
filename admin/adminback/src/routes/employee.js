const express = require('express');
const router = express.Router();

const db = require('../database')

router.get('/', (req,res)=>{
    res.send('Employees');
})

router.post('/', (req,res)=>{
    console.log(req)
    res.send(received)
})

module.exports = router;