const axios = require('axios')

// axios.get('http://localhost:8000').then((res)=>{
//     console.log(res.data)
// })

axios.post('http://localhost:8000',{
    username: "Hello",
    password: "World"
})

console.log("DONE")