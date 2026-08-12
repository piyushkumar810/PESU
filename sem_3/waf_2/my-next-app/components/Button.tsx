// Function Prop Example

interface ButtonProps {
    label: string;
    onClick: () => void;
}

function Button({ label, onClick }: ButtonProps): string {
    onClick();

    return label;
}

export default Button;