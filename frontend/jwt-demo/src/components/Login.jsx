import {Link} from 'react-router-dom'
export function Login() {
    return (
        <div>
            <h3>ログイン</h3>
            <form onSubmit={handleLoginSubmit}>
                <div className="input-container">
                    <label>ユーザー名 </label>
                    <input type="text" name="uname" required />
                </div>
                <div className="input-container">
                    <label>パスワード </label>
                    <input type="password" name="pass" required />
                </div>
                <div className="button-container">
                    <input type="submit" />
                </div>
            </form>
            <Link to={"/"}>まだアカウントを持っていない場合はこちら</Link>
        </div>
    );
}

const handleLoginSubmit = () => {
    return true
}