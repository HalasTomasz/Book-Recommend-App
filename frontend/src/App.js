import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import PrivateRoute from './utilitis/PrivateRoute';
import Navbar from './components/NavBar';
import {AuthProvider} from './context/AuthContext'
import Login from './components/Login';
import Signup from './components/SignUp';
import ForgotPassword from './components/ForgotPassword';

function App() {
  return (
    <Router>
    <AuthProvider>
      <Routes >
        <Route path="/" element={
          <PrivateRoute>
             <Navbar />
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
