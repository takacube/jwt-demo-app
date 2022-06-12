import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Top from './components/Top';
import { Login } from './components/Login';
import { MyPage } from './components/MyPage';

function App() {
    return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Top />} />
            <Route path="login" element={<Login />} />
            <Route path="mypage" element={<MyPage />} />
        </Routes>
    </BrowserRouter>
    )
}

export default App;
