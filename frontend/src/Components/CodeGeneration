import { useState } from "react";

function CodeGeneration() {
  const [inputText, setInputText] = useState("")
  const [language, setLanguage] = useState("python")
  const [outputCode, setOutputCode] = useState("")

  const handleGenerate = async () => {
    try{
      const response = await fetch("https://a0b9-34-73-33-8.ngrok-free.app/generate",{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          prompt: inputText,
          max_tokens: 128
        }),
      });

      const data = await response.json();
      setOutputCode(data.code);
    } catch (error){
      console.error("API呼び出しエラー:", error);
      setOutputCode("エラーが発生しました。Colab側が起動しているか確認してください。");
    }
  };

  return (
    <div style={{ paddingLeft: "2rem",fontFamily: "sans-serif" }} >
      <h1>問題演習</h1>
      
      <label>問題文を入力</label>
      <br />
      <textarea
        rows={10}
        cols={100}
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="ここに問題文を入力..."
        style={{ marginBottom: "1rem", width: "100%"}}
      />

      <br />
      <label>言語選択:</label>
      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        style={{marginLeft: "1rem"}}
      >
        <option value="python">Python</option>
        <option value="cpp">C++</option>
        <option value="java">Java</option>
        <option value="R">R</option>
      </select>

      <br /><br />
      <button onClick={handleGenerate}>模範解答</button>
      
      <h2>出力コード : </h2>
      <pre
        style={{
          background: "#f5f5f5",
          padding: "1rem",
          color: "#222",
          fontFamily: "monospace",
          borderRadius: "5px",
          whiteSpace: "pre-wrap"
        }}
      >
        {outputCode}
      </pre>
    </div>
  );
}

export default CodeGeneration;
