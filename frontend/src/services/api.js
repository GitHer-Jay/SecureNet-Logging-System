import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const addLog = (data) =>
  API.post("/log", null, { params: data });

export const verifyLogs = () =>
  API.get("/verify");

export const getLogs = () =>
  API.get("/logs");