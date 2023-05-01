import { useState, useRef } from "react";

export default function FilePreviewer() {
  const [videoPreview, setVideoPreview] = useState(null);
  const filePicekerRef = useRef(null);

  const previewFile = e => {
    e.preventDefault();
    // Reading New File (open file Picker Box)
    const reader = new FileReader();
    // Gettting Selected File (user can select multiple but we are choosing only one)
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      reader.readAsDataURL(selectedFile);
    }
    // As the File loaded then set the stage as per the file type
    reader.onload = (readerEvent) => {
      if (selectedFile.type.includes("video")) {
        setVideoPreview(readerEvent.target.result);
      }
    };
  }

  const clearFile = e => {
    e.preventDefault();
    setVideoPreview(null);
  }
  
  return (
    <div>
      <div className="btn-container">
        <input ref={filePicekerRef} accept="video/*" onChange={previewFile} type="file" hidden />
        <button className="btn" onClick={() => filePicekerRef.current.click()}>
          {videoPreview == null ? 'Upload File' : 'Upload Another File'}</button>
        <button className="btn" onClick={clearFile}>x</button>
      </div>
      <div className="preview">
        {videoPreview != null && <video controls src={videoPreview}></video>}
      </div>
    </div>
  );
}