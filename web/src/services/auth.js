import {
  clearAuthTokens,
  setAuthTokens,
  useAuthTokenInterceptor,
} from "axios-jwt";

import axios from "axios";
import api from "./api";

const refreshEndpoint = `http://localhost:8000/v1/auth/refresh_token/`;

export const authResponseToAuthTokens = (res) => ({
  accessToken: res.access_token,
  refreshToken: res.refresh_token,
});

const requestRefresh = async (refreshToken) => {
  try {
    const access = await axios.post(refreshEndpoint, { refresh: refreshToken }).then(resp => {
      return resp.data.access
    })
    return access;
  } catch (err) {
    // TODO: Add error handling
    console.log(err);
  }
};

useAuthTokenInterceptor(api, { requestRefresh });

export const processFacebookResponse = ({ accessToken }) => {
  api
    .post("auth/login/", JSON.stringify({ access_token: accessToken }))
    .then((response) => response.data)
    .then((data) => {
      setAuthTokens(authResponseToAuthTokens(data));
    })
    .catch((error) => {
      console.log(error);
    });
};

export const logout = (setUser) => {
  clearAuthTokens();
};
