BASE_COVER_LETTER = """Dear Hiring Manager,

I am excited to apply for the position at your company. With over five years of experience in software development, I have built and maintained web and mobile applications using a variety of technologies including React, Node.js, and Python.

In my previous role at AcmeTech, I led a team of developers to deliver scalable solutions for high-traffic applications. I pride myself on writing clean, maintainable code and collaborating effectively with cross-functional teams.

I am enthusiastic about the opportunity to contribute my skills and experience to your organization and am confident that I can help achieve your technical goals.

Thank you for your time and consideration. I look forward to the possibility of discussing my application further.

Sincerely,  
Alex Johnson  
alex.johnson@example.com  
(555) 123-4567
"""


def build_cover_letter_prompt(job_description):
    return f"""
    You are an expert career writer and hiring manager. Rewrite the following cover letter
    so it aligns directly with the job requirements found in the scraped Indeed job description.
    
    Instructions:
    - Clean and interpret the job description even if it contains noise or formatting issues.
    - Identify required skills, responsibilities, and tone.
    - Rewrite the cover letter to emphasize the applicant's most relevant strengths.
    - Preserve the applicant’s voice and background.
    - Remove irrelevant content.
    - Improve clarity, structure, and professionalism.
    - Output only the final polished cover letter.
    
    ### JOB DESCRIPTION 
    {job_description}
    
    ### ORIGINAL COVER LETTER
    {BASE_COVER_LETTER}
    
    ### UPDATED COVER LETTER (TAILORED TO JOB)
    """
