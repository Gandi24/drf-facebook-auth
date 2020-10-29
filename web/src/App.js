import React from "react";
import "./App.css";
import Auth from "./components/Auth";
import UserDetails from "./components/UserDetails";

const App = () => {
  return (
    <div className="App">
      <Auth />
      <UserDetails />
    </div>
  );
};

export default App;
