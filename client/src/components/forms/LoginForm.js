import { useState } from "react";

export default function LoginForm( {onSubmit} ){

    const [user, setUser] = useState({username:"", password:""})

    function handleChange(e){
        setUser({
            ...user,
            [e.target.name]: e.target.value
        })

    }

    return (
        <form id="login-form" onSubmit={(e) => {onSubmit(e, user)}}>
            <div>
                <label htmlFor="username">UserName : </label>
                <input id="username" name="username" type="text" placeholder="username" onChange={handleChange}/>
            </div>
            <div>
                <label htmlFor="password">password : </label>
                <input id="password" name="password" type="password" placeholder="password" onChange={handleChange}/>
            </div>
            <button id="login-submit" type="submit">Submit</button>
        </form>
    )

}