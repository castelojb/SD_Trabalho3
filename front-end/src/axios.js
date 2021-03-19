import Axios from "axios";
import { message } from "antd";

const axios = Axios.create();

const DisplayError = errorMessage => {
  message.error(errorMessage);
};

const ErrorResponseHandler = err => {
  console.log(err);
  DisplayError(err.message);
  return Promise.reject(err);
};

axios.interceptors.response.use(res => res, ErrorResponseHandler);

export default axios;
