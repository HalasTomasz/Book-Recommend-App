import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import PrivateRoute from './utilitis/PrivateRoute';
import Navbar from './components/NavBar';
import {AuthProvider} from './context/AuthContext'
import Login from './components/Login';
import Signup from './components/SignUp';
import ForgotPassword from './components/ForgotPassword';
import HomeS from './pages/HomeS';
import BookS from './pages/BookS';
import SearchBar from './components/SearchBar';
import Profil from './components/UserProfile';
import HistoryS from './pages/HistoryS';

function App() {
  return (
    <Router>
    <AuthProvider>
      <Routes >
        <Route path="/" element={
          <PrivateRoute>
             <Navbar />
             <HomeS />
          </PrivateRoute>
          }
        ></Route>
        <Route path='/books/:id' element={
          <PrivateRoute>
             <Navbar />
             <BookS />
          </PrivateRoute>
          }
        ></Route>
          <Route path='/search' element={
          <PrivateRoute>
             <Navbar />
            <SearchBar />
          </PrivateRoute>
          }
        ></Route>
        <Route path='/user' element={
          <PrivateRoute>
             <Navbar />
             <Profil />
          </PrivateRoute>
          }
        ></Route>
        <Route path='/history' element={
          <PrivateRoute>
             <Navbar />
             <HistoryS /> 
          </PrivateRoute>
          }
        ></Route>
        <Route path='/login' element={<Login/>} />
        <Route path='/signup' element={<Signup/>} />
        <Route path='/forgot-password' element={<ForgotPassword/>} />
      </Routes>
    </AuthProvider>
  </Router>
  );
}

export default App;
