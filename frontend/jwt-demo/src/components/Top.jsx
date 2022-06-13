import {Link} from 'react-router-dom'
import axios from 'axios';
import { useState } from 'react';

const Top = () => {
    const [user, setUser] = useState([]);
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const HandleSubmit = () => {
        setUser([...user, { name: name, password: password }]);
        axios.post("http://localhost:8001/subscription", user)
        .then(res => {
            console.log(res)
        })
    }
    return (
        <div>
            {JSON.stringify({user})}
            {name}{password}
            <h3>ユーザー登録</h3>
            <form onSubmit={HandleSubmit}>
                <div className="input-container">
                    <label>ユーザー名 </label>
                    <input type="text" name="uname" value={name} onChange={(event) => setName(event.target.value)} required />
                </div>
                <div className="input-container">
                    <label>パスワード </label>
                    <input type="password" name="pass" value={password} onChange={(event) => setPassword(event.target.value)} required />
                </div>
                <div className="button-container">
                    <input type="submit" />
                </div>
            </form>
            <Link to={"/login/"}>すでに登録済みの方はこちら</Link>
        </div>
    );
}




export default Top;