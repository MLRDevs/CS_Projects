// Alex Miller
// component for removing tasks


import { useDroppable } from "@dnd-kit/core";
import { FaTrashAlt } from 'react-icons/fa';

const Trashcan = () => {
    const { setNodeRef, isOver } = useDroppable({
        id: 'trash',
    });

    return (

        <div
            ref={setNodeRef}
            className={`p-4 rounded-full transition-colors ${
                isOver ? 'bg-red-700' : 'bg-red-500'
            }`}
            title="Drag here to delete"
        >
            <FaTrashAlt size={30} color="white" />
        </div>
    )
}

export default Trashcan;




