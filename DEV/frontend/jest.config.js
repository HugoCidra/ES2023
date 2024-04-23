module.exports = {
    verbose: true,
    testEnvironment: 'jsdom',
    transform: {
      '\\.js$': 'babel-jest',
    },
    moduleNameMapper: {
      '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
      '\\.(jpg|jpeg|png|gif|webp|svg)$': '<rootDir>/__mocks__/fileMock.js',
    },
    transformIgnorePatterns: [
        '/node_modules/(?!(axios)/)',
    ],
};