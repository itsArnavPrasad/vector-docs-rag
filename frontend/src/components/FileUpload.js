import { useState } from "react";
import { uploadPDF } from "../api";

export default function FileUpload({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const res = await uploadPDF(file);
    onUpload(res.data);
    setFile(null);
  };

  return (
    <div className="flex gap-2 items-center">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded"
        onClick={handleUpload}
      >
        Upload PDF
      </button>
    </div>
  );
}
