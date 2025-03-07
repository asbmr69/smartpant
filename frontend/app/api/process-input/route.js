export async function POST(request) {
    try {
      const { input } = await request.json();
  
      // Forward the input to the backend server
      const backendResponse = await fetch("http://localhost:8000/chat/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
          message: input, }),
      });
      console.log("Backend Response Status:", backendResponse.status);
      console.log("Backend Response Body:", await backendResponse.json());
      
      if (!backendResponse.ok) {
        throw new Error("Backend server error");
      }
  
      const result = await backendResponse.json();
      return Response.json({ result });
    } catch (error) {
      console.error("Error processing input:", error);
      return Response.json({ error: "Failed to process input" }, { status: 500 });
    }
  }