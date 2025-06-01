// Alex Miller
// component holding the container of tasks

import type { Item } from "../types/Item";
import TaskItem from './TaskItem';
import { useDroppable } from '@dnd-kit/core';


type Props = {
    title: string;
    items: Item[];
    color: string;
    containerId: string;
};


const TaskContainer: React.FC<Props> = ({ title, containerId, items, color }) => {

    const { setNodeRef } = useDroppable({
        id: containerId,
    });

    return (
        <div className={color}>
            <h2 className="text-2xl font-bold text-black">{title}</h2>
            <div 
                className=" m-10 bg-white h-100 overflow-y-scroll overflow-x-hidden"
                ref={setNodeRef}
            >
                <ul className="text-white text-left px-2 py-10 overflow-x-hidden overflow-y-hidden">
                    {items.map(item => (
                        <TaskItem key={item.id} item={item} />
                    ))}
                </ul>
            </div>
            
        </div>
    )
}

export default TaskContainer;




