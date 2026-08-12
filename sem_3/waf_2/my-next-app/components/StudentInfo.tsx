interface StudentInfoProps {
    name: string;
    age: number;
    course: string;
    subjects: string[];
}

function StudentInfo({
    name,
    age,
    course,
    subjects
}: StudentInfoProps): string {

    return `
Name: ${name}
Age: ${age}
Course: ${course}
Subjects: ${subjects.join(", ")}
`;
}

export default StudentInfo;