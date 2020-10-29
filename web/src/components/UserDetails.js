import React, {useState} from "react";
import api from "../services/api";

const UserDetails = () => {
  const [user, setUser] = useState({});

  const getUserDetails = () => {
    api.get("me/")
    .then((data) => {
      setUser(data.data);
    })
    .catch((error) => {
      setUser({});
    });
  };

  return (
    <div className="UserDetails">
      <button onClick={getUserDetails}>Get user details</button>
      <br />
      {user.profile_image && (
        <img
          src={user.profile_image}
          width={200}
          height={200}
          alt={"Profile"}
        />
      )}
      <p>
        {user.first_name} {user.last_name}
      </p>
      <p>{user.email}</p>
    </div>
  );
};

export default UserDetails;
