type ChildContent = string | string[];

interface CardProps {
    title: string;
    children: ChildContent;
}

function Card({ title, children }: CardProps): string {
    const content = Array.isArray(children)
        ? children.join(" ")
        : children;

    return `${title}: ${content}`;
}

export default Card;