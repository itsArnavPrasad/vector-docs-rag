import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000", // Adjust if backend is elsewhere
});

export const uploadPDF = (file) => {
  console.log("Uploading file:", file);
  const formData = new FormData();
  formData.append("file", file);
  return API.post("/upload-pdf", formData);
};

export const buildIndex = () => {
  return API.post("/build-index");
};

export const queryRAG = (q) => {
  return API.get("/rag-answer", { params: { q } });
};

export const getFiles = () => {
  return API.get("/list-files"); 
};
