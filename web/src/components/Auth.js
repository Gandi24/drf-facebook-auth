import React from "react";
import FacebookLogin from "react-facebook-login";
import { logout, processFacebookResponse } from "../services/auth";

const GRAPH_OBJECT_SCOPES = [
];


const GRAPH_OBJECT_FIELDS = [
  "gender",
];

const Auth = () => {
  return (
    <div className="Auth">
      <FacebookLogin
        appId={process.env.REACT_APP_FACEBOOK_APP_ID}
        fields={GRAPH_OBJECT_FIELDS.join(",")}
        scope={GRAPH_OBJECT_SCOPES.join(",")}
        callback={(response) => processFacebookResponse(response)}
      />
      <button onClick={() => logout()}>Logout</button>
    </div>
  );
};

export default Auth;
