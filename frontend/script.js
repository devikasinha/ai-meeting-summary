// Simulated transcription & MOM (replace with AI backend later)

// Demo transcription text
const demoTranscript = `
John: Welcome everyone to the weekly project meeting.
Sarah: The new feature is almost complete, we need testing.
Mike: Deadline should be extended by 3 days due to delays.
`;

// Demo MOM text
const demoMOM = `
Attendees: John, Sarah, Mike

Key Discussions:
- Project progress reviewed.
- Feature development nearly complete.
- Testing required before final release.

Decisions:
- Extend deadline by 3 days.

Action Items:
- Sarah to oversee testing.
- Mike to update timeline.
`;

document.getElementById("processBtn").addEventListener("click", () => {
  // For now we simulate transcript + MOM
  document.getElementById("transcriptBox").value = demoTranscript;
  document.getElementById("momBox").value = demoMOM;
});

// PDF Download
document.getElementById("downloadPdf").addEventListener("click", () => {
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();

  let momText = document.getElementById("momBox").value;

  doc.setFont("helvetica");
  doc.setFontSize(12);
  doc.text(momText, 10, 10);

  doc.save("MOM.pdf");
});
