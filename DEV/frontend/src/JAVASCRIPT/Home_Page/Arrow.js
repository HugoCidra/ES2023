import React, { useEffect, useState } from 'react';
import Seta from '../../IMAGES/seta.png'
import '../index.css'
import './Arrow.css'

export default function Arrow() {
    const [opacity, setOpacity] = useState(1);
    const [isAtBottom, setIsAtBottom] = useState(false); // Add new state for tracking if component is at the bottom

    const handleScroll = () => {
        const scrollPosition = window.innerHeight + window.pageYOffset;
        const documentHeight = document.documentElement.scrollHeight;

        const maxOpacity = 1;
        const minOpacity = 0;

        const distanceFromBottom = documentHeight - scrollPosition;
        const opacityValue = distanceFromBottom / window.innerHeight;
        const newOpacity = Math.max(minOpacity, Math.min(maxOpacity, opacityValue));

        setOpacity(newOpacity);

        // Check if component is at the bottom of the page
        if (distanceFromBottom <= 3) {
            setIsAtBottom(true);
        } else {
            setIsAtBottom(false);
        }
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    const scrollToBottom = () => {
        window.scrollTo({
            top: document.documentElement.scrollHeight,
            behavior: 'smooth'
        });
    };

    return (
        <>
        <div className={`arrow ${isAtBottom ? 'hidden' : ''}`} onClick={scrollToBottom} style={{ opacity }}>
            <img src={Seta} alt="arrow" />
        </div>
        </>
    );
}
