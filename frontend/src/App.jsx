import React from "react";
import Register from "./components/registerComponent/register";
import HomeComp from "./components/homeComp";
import Login from './views/login/login'
import { Route, Routes } from "react-router-dom";
import "./App.css";
import Profile from "./views/profile/profile";

function App() {


  return (
    <>
      <Routes>
        <Route path="/" element={<HomeComp />} />
        <Route path='/login' element={<Login />}/>
        <Route path="/register" element={<Register />} />
        <Route path="/explore" element={<h1>Explore</h1>} />
        <Route path="/publish" element={<h1>Publish</h1>} />
        <Route path="/notifications" element={<h1>Notifications</h1>} />
        <Route path="/profile/:id" element={<Profile />} />
      </Routes>
    </>
  );
}

export default App;

// pet={perfiles}