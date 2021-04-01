import express from 'express'
import fetch from 'node-fetch'
const app = express()

const client_id = process.env.INAT_CLIENT_ID
const client_secret = process.env.INAT_CLIENT_SECRET

console.log({client_id, client_secret})

app.get('/', (req, res) => {
    res.send('Test')
})

app.get('/login/iNat', (req, res) => {
    const url = `https://www.inaturalist.org/oauth/authorize?client_id=${client_id}&redirect_uri=http://localhost:9000/login/iNat/callback&response_type=code`
    res.redirect(url)
} )

async function getAccessToken(code) {
    
    const res = await fetch(`https://www.inaturalist.org/oauth/token?client_id=${client_id}&client_secret=${client_secret}&code=${code}&redirect_uri=http://localhost:9000/login/iNat/callback&grant_type=authorization_code`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            client_id,
            client_secret,
            code
        })
    })
    const data = await res.json()
    const params = new URLSearchParams(data)
    return params.get('access_token')
}

async function getiNatUser (access_token) {

    const req = await fetch(`https://www.inaturalist.org/users/edit.json`, {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${access_token}`
        }
    })
    console.log(req)
    const data = await req.json()
    return data
    //v1/users/me
}

app.get('/login/iNat/callback', async (req, res) => {
    const code = req.query.code;
    const token = await getAccessToken(code);
    const iNatData = await getiNatUser(token);
    //res.json({token})
    //console.log(token)
    res.json(iNatData);
} );

app.get('/home', (req, res) => {
    console.log(token)
})

const PORT = process.env.PORT || 9000;
app.listen(PORT, () => console.log('Listening http://localhost:' + PORT))