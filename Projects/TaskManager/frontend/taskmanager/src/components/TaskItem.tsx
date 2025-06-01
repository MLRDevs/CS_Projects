// Alex Miller
// Task item in list


import { useDraggable } from "@dnd-kit/core";
import type { Item } from '../types/Item';

type Props = {
    item: Item;
};

const TaskItem: React.FC<Props> = ({ item }) => {
    const { attributes, listeners, setNodeRef, transform, isDragging } = useDraggable({
        id: item.id,
        data: { item },
    });

    const style = { 
        transform : transform
        ? `translate(${transform.x}px, ${transform.y}px)`
        : undefined,
        opacity: isDragging ? 0 : 1,
    }

    return (

        <div
            ref={setNodeRef}
            style={style}
            {...listeners}
            {...attributes}
            className="bg-gray-900 m-2 px-2 cursor-move"
        >
            <li className="text-lg font-bold">
                {item.title}
                <div className="text-sm font-semibold text-gray-400">
                    {item.description}
                </div>
            </li>

        </div>
    )
}

export default TaskItem;




