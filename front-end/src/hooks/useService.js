import axios from "../axios";
import { message } from "antd";

axios.interceptors.request.use(
  request => request,
  error => {
    message.error(error.message);
    return Promise.reject(error);
  }
);

const baseUrl = process.env.REACT_APP_URL;
const useService = () => {
  const getEquipments = (setEquipments, setError, setLoading) => {
    setLoading(true);
    axios
      .get(baseUrl)
      .then(results => {
        setEquipments(results.data);
      })
      .catch(err => {
        setError(err);
      })
      .finally(() => {
        setLoading(false);
      });
  };
  const changeStatus = (
    id,
    status,
    type,
    setEquipment,
    setError,
    setLoading
  ) => {
    setLoading(true);
    axios
      .put(baseUrl + "/" + id, { status, type })
      .then(results => {
        setEquipment(results.data);
      })
      .catch(err => {
        setError(err);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return {
    getEquipments,
    changeStatus,
  };
};

export default useService;
