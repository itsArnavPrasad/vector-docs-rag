import { useState, useEffect } from "react";
import FileUpload from "./components/FileUpload";
import FileList from "./components/FileList";
import BuildIndex from "./components/BuildIndex";
import QueryRAG from "./components/QueryRAG";
import AnswerDisplay from "./components/AnswerDisplay";
import { getFiles } from "./api";

function App() {
  const [files, setFiles] = useState([]);
  const [answer, setAnswer] = useState("");

  const refreshFiles = async () => {
    const res = await getFiles();
    setFiles(res.data.files);
  };

  useEffect(() => {
    refreshFiles();
  }, []);

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">VectorDocs RAG</h1>
      <FileUpload onUpload={refreshFiles} />
      <FileList files={files} />
      <BuildIndex />
      <QueryRAG onAnswer={setAnswer} />
      <AnswerDisplay answer={answer} />
    </div>
  );
}

export default App;
