var fs = require('fs')

fs.readFileSync('./config.env', 'utf-8', (err, data)=>{
    if(!err){
        console.log(data)
    }
})

switch(process.env.NODE_ENV){
    case 'development': {
        console.log("development environment")
        process.env.HOST='localhost'
        process.env.PORT='8080'
        break
    }
    case 'production': {
        console.log("productions environment")
        process.env.HOST='www.site.com.br'
        process.env.PORT='80'
        break
    }
    default:{
        console.log("Any environoment environment")
    }
}

console.log(process.env.HOST)