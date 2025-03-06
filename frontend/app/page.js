"use client";
import { useState, useCallback, useEffect } from "react";
import axios from "axios";

// Helper components for displaying messages
const HumanMessage = ({ text }) => (
  <div className="flex justify-end">
    <div className="bg-blue-600 text-black rounded-lg p-3 max-w-[70%] shadow-sm">
      <p className="text-sm">{text}</p>
    </div>
  </div>
);

const GeminiMessage = ({ text }) => (
  <div className="flex justify-start">
    <div className="bg-white text-gray-900 rounded-lg p-3 max-w-[70%] shadow-sm">
      <p className="text-sm">{text}</p>
    </div>
  </div>
);

export default function Home() {
  const [input, setInput] = useState(""); // User input
  const [messages, setMessages] = useState([]); // Chat history
  const [isLoading, setIsLoading] = useState(false); // Loading state

  // Handle user input submission
  const handleSubmit = useCallback(async () => {
    if (!input.trim()) return; // Ignore empty input

    setIsLoading(true);
    setMessages((prev) => [...prev, { type: "human", text: input }]); // Add user message to chat history

    try {
      // Send input to the backend API
      const response = await axios.post("/api/process-input", { input });
      const result = response.data.result;

      // Add Gemini response to chat history
      setMessages((prev) => [...prev, { type: "gemini", text: result }]);
    } catch (error) {
      console.error("Error processing input:", error);
      setMessages((prev) => [...prev, { type: "gemini", text: "Error processing your request. Please try again." }]);
    } finally {
      setIsLoading(false);
      setInput(""); // Clear input field
    }
  }, [input]);

  const handleEnterSubmit = useCallback(async () => {
    if (!input.trim()) return; // Ignore empty input

    setIsLoading(true);
    setMessages((prev) => [...prev, { type: "human", text: input }]); // Add user message to chat history

    try {
      // Send input to the backend API (using /answer endpoint)
      const response = await axios.post("/api/answer", { input });
      const result = response.data.result;

      // Add Gemini response to chat history
      setMessages((prev) => [...prev, { type: "gemini", text: result }]);
    } catch (error) {
      console.error("Error processing input:", error);
      setMessages((prev) => [...prev, { type: "gemini", text: "Error processing your request. Please try again." }]);
    } finally {
      setIsLoading(false);
      setInput(""); // Clear input field
    }
  }, [input]);

  // Add event listener for the Enter key
  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === "Enter" && !isLoading) {
        handleEnterSubmit();
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [handleEnterSubmit, isLoading]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-blue-100 flex">
      {/* Sidebar */}
      <div className="w-64 bg-white border-r border-gray-200 p-6 shadow-sm">
        <h1 className="text-xl font-bold text-gray-900">Multimodal LLM</h1>
        <p className="text-sm text-gray-500 mt-2">Assistant at service</p>
      </div>

      {/* Main Chat Window */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <div className="bg-white border-b border-gray-200 p-6 shadow-sm">
          <h2 className="text-lg font-semibold text-gray-900">Chat</h2>
        </div>

        {/* Chat History */}
        <div className="flex-1 p-6 overflow-y-auto">
          <GeminiMessage text="Hi! I'm Multimodal LLM. How can I assist you today?" />
          {messages.map((message, index) =>
            message.type === "human" ? (
              <HumanMessage key={`msg-${index}`} text={message.text} />
            ) : (
              <GeminiMessage key={`msg-${index}`} text={message.text} />
            )
          )}
        </div>

        {/* Input Area */}
        <div className="bg-white border-t border-gray-200 p-6 shadow-lg">
          <div className="flex gap-2 max-w-2xl mx-auto">
          <button
      className="p-2 text-gray-500 hover:text-gray-700"
      onClick={() => alert("Voice input not yet implemented")}
    >
      🎤
    </button>
    <button
      className="p-2 text-gray-500 hover:text-gray-700"
      onClick={() => alert("Image input not yet implemented")}
    >
      📷
    </button>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your query..."
              className="flex-1 px-4 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
              disabled={isLoading}
            />
            <button
              onClick={handleSubmit}
              disabled={isLoading}
              className="px-6 py-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-blue-400"
            >
              {isLoading ? "Processing..." : "Send"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}