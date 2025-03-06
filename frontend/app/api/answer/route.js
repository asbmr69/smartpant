export async function POST(request) {
    try {
      const { input } = await request.json();
  
      // Forward the input to the backend API
      const backendResponse = await fetch("http://localhost:8000/answer/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input }),
      });
  
      if (!backendResponse.ok) {
        throw new Error("Backend server error");
      }
  
      const result = await backendResponse.json();
      return Response.json({ result: result.result });
    } catch (error) {
      console.error("Error processing input:", error);
      return Response.json({ error: "Failed to process input" }, { status: 500 });
    }
  }